function twoArePositive(a, b, c) {
    return Array.from([a, b, c]).filter(n => n > 0).length  === 2 ? true : false ;
  }


  function eliminateUnsetBits(number) {
    //return parseInt(number.replace(/0/g,'') || 0, 2)
    return parseInt(number.replaceAll('0', ''), 2);

  }

  eliminateUnsetBits("11010101010101")
  //twoArePositive(2, 4, -3)