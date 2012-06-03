var worker = self;

(function() {

var ColorSetter = function(width, height) {
  this.colors = new Float32Array(width * height * 4);
  
  this.setPixels = function(callback) {
    var length = width * height;
    for (var i=0; i<length; ++i) {
      var x = i%width, y = parseInt(i/width);
      var colors = callback(x, y);
      this.colors[i*4] = colors[0];
      this.colors[i*4+1] = colors[1];
      this.colors[i*4+2] = colors[2];
      this.colors[i*4+3] = colors[3] || 255;
    }
  };
};

worker.onmessage = function(event) {
  var data = event.data;
  if (data) {
    data.definition = data.definition || 'return [ 255, 255, 255 ]';
    var colorSetter = new ColorSetter(data.width, data.height);
    var callback = getFunction(data.definition, data.width, data.height);
    colorSetter.setPixels(callback);
    worker.postMessage({ colors: colorSetter.colors });
  }
};

var getFunction = function(definition, width, height) {
    var worker = undefined;
    var ColorSetter = undefined;
    eval('var definition = undefined; function setPixels(x, y) {' + definition + '}');
    return setPixels;
};

})();