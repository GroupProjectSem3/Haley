const isEmpty = require("is-empty");
module.exports= function validateFPwdData (data) {
    let errors = {};
  
    if (isEmpty(data.email)) errors.email = 'Must not be empty';
  
    return {
      errors,
      valid: Object.keys(errors).length === 0 ? true : false
    };
  };