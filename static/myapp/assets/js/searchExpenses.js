const searchField=document.querySelector("#searchField");

const appTable=document.querySelector(".app-table");
const tableOutput=document.querySelector(".table-output");
tableOutput.style.display='none'
const paginationContainer = document.querySelector(".pagination-container");
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector(".table-body");

searchField.addEventListener('keyup', (e)=>{
    const searchValue=e.target.value;

    if(searchValue.trim().length > 0) {
        console.log("searchValue", searchValue);

        paginationContainer.style.display = "none";
        tbody.innerHTML = "";
        fetch("/search_expenses", {
            body: JSON.stringify({searchText: searchValue}),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                
                appTable.style.display = "none";
                tableOutput.style.display = "block";

                if(data.length==0){
                    noResults.style.display = "block";
                    tableOutput.style.display = "none";
                }else {
                    noResults.style.display = "none";
                    data.forEach((expense) =>{
                        tbody.innerHTML += `
                        <tr> 
                            <td>
                                <div class="d-flex px-2 py-1">
                                    <div class="d-flex flex-column justify-content-center">
                                        <h6 class="mb-0 text-sm">${expense.amount}</h6>
                                        <p class="text-xs text-secondary mb-0">john@creative-tim.com</p>
                                    </div>
                                </div>
                            </td>
                            <td>
                                <span class="badge badge-sm bg-gradient-success">${expense.category}</span>
                            </td>
                            <td class="align-middle text-center text-sm">
                                <p class="text-xs font-weight-bold mb-0">${expense.description}</p>
                       
                            </td>
                            <td class="align-middle text-center">
                                <span class="text-secondary text-xs font-weight-bold">${expense.date}</span>
                            </td>
                        </tr>`;
                    })

                }
            });
    } else {
        tableOutput.style.display = "none";
        appTable.style.display = "block";
        paginationContainer.style.display = "block";
    }
    

});