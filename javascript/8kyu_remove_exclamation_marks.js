function removeExclamationMarks(s) {
    return s.replace(new RegExp("!", 'g'),"");
  }
removeExclamationMarks("Hello World!")