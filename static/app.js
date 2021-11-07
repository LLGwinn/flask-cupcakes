const BASE_URL = "http://localhost:5000/api";

function generateCupcakeHTML(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          ${cupcake.flavor} - ${cupcake.size} - Rating: ${cupcake.rating}
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)"
              width="100px">
      </div>
    `;
  }


async function showStartingCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);
    const allCupcakes = response.data.cupcakes;
  
    for (let cupcake of allCupcakes) {
      let newCupcake = $(generateCupcakeHTML(cupcake));
      $('ul').append(newCupcake);
    }
  }

  $("form").on("submit", async function (evt) {
    evt.preventDefault();
  
    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    let image = $("#image").val();
  
    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });
  
    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("ul").append(newCupcake);
    $("form").trigger("reset");
  });

showStartingCupcakes();