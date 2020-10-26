const form = document.getElementById('form');
const power_consumption = document.getElementById('power_consumption');
const hours_per_month_usage = document.getElementById('hours_per_month_usage');
const repair_price = document.getElementById('repair_price');
const location_in_house = document.getElementById('location_in_house');
const appliance_name = document.getElementById('appliance_name');
const plugged_into_socket = document.getElementById('plugged_into_socket');
const connection_protocol = document.getElementById('connection_protocol');
const data_transfer_amount = document.getElementById('data_transfer_amount');

function showError(input, message) {
  const formControl = input.parentElement;
  formControl.className = 'form-control error';
  const small = formControl.querySelector('small');
  small.innerText = message;
}

function showSuccess(input) {
  const formControl = input.parentElement;
  formControl.className = 'form-control success';
}

function checkRequired(inputArr) {
  let isRequired = false;
  inputArr.forEach(function(input) {
    if (input.value.trim() === '') {
      showError(input, `${getFieldName(input)} is required`);
      isRequired = true;
    } else {
      showSuccess(input);
      return true;
    }
  });

  return isRequired;
}

function checkFloat(input){
  const re = /^[0-9]+\.?[0-9]*$/;
  if (re.test(input.value.trim())) {
    showSuccess(input);
    return true;
  } else {
    showError(input, 'This field should contain float');
    return false;
  }
}

function checkInt(input){
  const re = /^[0-9]+$/;
    if (re.test(input.value.trim())) {
      showSuccess(input);
      return true;
    } else {
      showError(input, 'This field should contain integer');
      return false;
    }
}

function checkBool(input){
  const re = /(1)|(0)/;
    if (re.test(input.value.trim())) {
      showSuccess(input);
      return true;
    } else {
      showError(input, 'This field should contain 1 or 0');
      return false;
    }
}

function checkStr(input){
  const re = /\w+/;
    if (re.test(input.value.trim())) {
      showSuccess(input);
      return true;
    } else {
      showError(input, 'This field should contain string');
      return false;
    }
}

function getFieldName(input) {
  return input.id.charAt(0).toUpperCase() + input.id.slice(1);
}

function checkform(){
  if(!checkRequired([power_consumption, hours_per_month_usage,
                              repair_price, location_in_house,
                              appliance_name, plugged_into_socket,
                              connection_protocol, data_transfer_amount])){
  return checkInt(power_consumption) &&
      checkFloat(hours_per_month_usage) &&
      checkFloat(repair_price) &&
      checkStr(location_in_house) &&
      checkStr(appliance_name) &&
      checkBool(plugged_into_socket) &&
      checkStr(connection_protocol) &&
      checkFloat(data_transfer_amount);
  }
  else {
    return false;
  }
}