const sequenceSum = (begin, end, step) => {

    // sequenceSum = (b, e, s) =>  b > e ? 0 : b + sequenceSum(b + s, e, s);
    let sum = 0;
    for (begin; begin <= end; begin +=step) { 
        sum +=begin;
      }
     return sum;
  };


  sequenceSum(2, 6, 2)//, 12