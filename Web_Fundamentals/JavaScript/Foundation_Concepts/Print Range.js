function printRange(rangeStart, rangeStop) {
    var text = "";
    for (var i = rangeStart; i <= rangeStop; i++) {
      text += i + ',';
    }
  
    return text.slice(0, -1);
  }
  
  document.write(printRange(1, 33, 15));