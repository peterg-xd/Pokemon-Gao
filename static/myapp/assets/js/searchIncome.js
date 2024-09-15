const incomeSearchField = document.querySelector("#incomeSearchField");

const incomeAppTable = document.querySelector(".income-app-table");
const incomeTableOutput = document.querySelector(".income-table-output");
incomeTableOutput.style.display = 'none';
const incomePaginationContainer = document.querySelector(".income-pagination-container");
const incomeNoResults = document.querySelector(".income-no-results");
const incomeTbody = document.querySelector(".income-table-body");

let controller; // To hold the AbortController instance
let debounceTimer; // For debouncing

incomeSearchField.addEventListener('keyup', (e) => {
    clearTimeout(debounceTimer); // Clear the previous timer

    debounceTimer = setTimeout(() => {
        const searchValue = e.target.value;

        if (controller) {
            controller.abort(); // Cancel the previous request
        }

        if (searchValue.trim().length > 0) {
            console.log("searchValue", searchValue);

            incomePaginationContainer.style.display = "none";
            incomeTbody.innerHTML = "";

            controller = new AbortController(); // Create a new AbortController
            fetch("/search_income", {
                body: JSON.stringify({ incomeSearchText: searchValue }),
                method: "POST",
                signal: controller.signal, // Pass the signal to fetch
            })
                .then((res) => res.json())
                .then((data) => {
                    console.log("data", data);

                    incomeAppTable.style.display = "none";
                    incomeTableOutput.style.display = "block";

                    if (data.length === 0) {
                        incomeNoResults.style.display = "block";
                        incomeTableOutput.style.display = "none";
                    } else {
                        incomeNoResults.style.display = "none";
                        data.forEach((income) => {
                            incomeTbody.innerHTML += `
                                <tr>
                                    <td>
                                        <div class="d-flex px-2 py-1">
                                            <div class="d-flex flex-column justify-content-center">
                                                <h6 class="mb-0 text-sm">${income.amount}</h6>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <span class="badge badge-sm bg-gradient-success">${income.source}</span>
                                    </td>
                                    <td class="align-middle text-center text-sm">
                                        <p class="text-xs font-weight-bold mb-0">${income.description}</p>
                                    </td>
                                    <td class="align-middle text-center">
                                        <span class="text-secondary text-xs font-weight-bold">${income.date}</span>
                                    </td>
                                </tr>`;
                        });
                    }
                })
                .catch((err) => {
                    if (err.name === 'AbortError') {
                        console.log('Fetch aborted');
                    }
                });
        } else {
            incomeTableOutput.style.display = "none";
            incomeAppTable.style.display = "block";
            incomePaginationContainer.style.display = "block";
        }
    }, 300); // Debounce delay of 300ms
});
