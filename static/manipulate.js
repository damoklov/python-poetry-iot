const main = document.getElementById('appliances');
const total = document.getElementById('total');
const sortBtn = document.getElementById('sort');
const calculatePowerConsumptionBtn = document.getElementById('calculate-consumption');
const trashImg = document.getElementById('trashImg');

let data = [];

getData();

async function getData() {
  const res = await fetch('http://127.0.0.1:5000/smart_home_appliance');
  const data = await res.json();
  const appliances = data.smart_home_appliances;

  for (let i = 0; i < appliances.length; i++) {
    if (typeof(appliances[i]) === 'object') {
      addData(appliances[i]);
    }
  }
}

function cleanData(){
  data = [];
}

function addData(obj) {
  data.push(obj);
}

function deleteAppliance(id){
  const formData = new FormData();
  let delete_endpoint = 'http://127.0.0.1:5000/smart_home_appliance/' + id;
  return fetch(delete_endpoint, {
        method: 'DELETE',
        body: formData
    }).then(response => response.json());
}

function formatPowerConsumption(number) {
  return number.toFixed(2);
}

function sortByUsage() {
  data.sort((a, b) => b._power_consumption - a._power_consumption);
  appliancesEl.innerHTML = data
  .map(
    appliance => `
  <div class="appliance">
    <h1>${appliance._appliance_name}</h1>
    <div class="appliance-info" data-applianceID="${appliance.id}">
      <h3>Location: ${appliance._location_in_house}</h3>
      <h3>Consumption: ${appliance._power_consumption}</h3>
      <h3><a href="/edit/${appliance.id}">#${appliance.id}</a><img alt="Delete" src="/static/trash.png" width="30" height="30" class="trashImg" onclick="deleteAppliance(${appliance.id})"/></h3>
    </div>
  </div>
`
  )
  .join('');
}

function calculatePowerConsumption() {
  const consumption = data.reduce((acc, user) => (acc += user._power_consumption), 0);
  const consumptionEl = document.createElement('div');

  consumptionEl.innerHTML = `<h2>Total Power Consumption: <strong>${formatPowerConsumption(
    consumption
  )}</strong></h2>`;
  total.innerHTML = '';
  total.appendChild(consumptionEl);
}

calculatePowerConsumptionBtn.addEventListener('click', calculatePowerConsumption);
sortBtn.addEventListener('click', sortByUsage);
trashImg.addEventListener('click', deleteAppliance);
