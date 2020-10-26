const search = document.getElementById('search');
const submit = document.getElementById('submit');
const appliancesEl = document.getElementById('appliances');
const resultHeading = document.getElementById('result-heading');
const singleAppliance = document.getElementById('single-appliance');

function searchAppliance(e) {
  e.preventDefault();
  singleAppliance.innerHTML = '';
  const term = search.value;

  if (term.trim()) {
    data = [];
    fetch(`http://127.0.0.1:5000/smart_home_appliance/search/${term}`)
      .then(res => res.json())
      .then(data => {
        resultHeading.innerHTML = `<h2>Search results for '${term}':</h2>`;

        if (data.smart_home_appliances === {}) {
            appliancesEl.innerHTML = `<p>There are no search results. Try again!<p>`;
        } else {
            for (let i = 0; i < data.smart_home_appliances.length; i++) {
                if (typeof(data.smart_home_appliances[i]) != 'undefined') {
                    addData(data.smart_home_appliances[i]);
        }
      }
          appliancesEl.innerHTML = data.smart_home_appliances
            .map(
              appliance => `
            <div class="appliance">
              <h1>${appliance._appliance_name} #${appliance.id}</h1>
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
      });
    search.value = '';
  } else {
      data = [];
        fetch(`http://127.0.0.1:5000/smart_home_appliance`)
          .then(res => res.json())
          .then(data => {
            resultHeading.innerHTML = '';

            if (data.smart_home_appliances === {}) {
                appliancesEl.innerHTML = `<p>There are no search results. Try again!<p>`;
            } else {
                for (let i = 0; i < data.smart_home_appliances.length; i++) {
                    if (typeof(data.smart_home_appliances[i]) != 'undefined') {
                        addData(data.smart_home_appliances[i]);
            }
          }
              appliancesEl.innerHTML = data.smart_home_appliances
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
          });
  }
}

function addData(obj) {
  data.push(obj);
}

submit.addEventListener('submit', searchAppliance);
trashImg.addEventListener('click', deleteAppliance);
