const Validator = require("validator");
const isEmpty = require("is-empty");
const isEmail = (email) => {
    const regEx = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (email.match(regEx)) return true;
    else return false;
  };
  const isPassword = (password) => {
    const reg = /^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})/;
    if(password.match(reg)) return true;
    else return false;
  }
module.exports = function validateRegisterInput(data) {
  let errors = {};
// Convert empty fields to an empty string so we can use validator functions

if (isEmpty(data.email)) {
  errors.email = 'Must not be empty';
} else if (!isEmail(data.email)) {
  errors.email = 'Must be a valid email address';
}

if (isEmpty(data.password)) {errors.password = 'Must not be empty';
}
// if (!Validator.isLength(data.password, { min: 6, max: 30 })) {
//   errors.password = "Password must be at least 6 characters";
// }
else if(!isPassword(data.password)){
  errors.password = "Password must contain atleast one lowercase,one uppercase,one numeric,one special and eight characters or longer "
}
if (data.password !== data.confirmPassword)
  errors.confirmPassword = 'Passwords must match';
if (isEmpty(data.handle)) errors.handle = 'Must not be empty';

return {
  errors,
  valid: Object.keys(errors).length === 0 ? true : false
};
};

