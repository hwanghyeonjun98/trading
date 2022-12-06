const sortBtn = document.querySelectorAll(".sort-btn");
const tableBody = document.querySelector("#data-table tbody");


sortBtn.forEach((btn) => {
	btn.addEventListener("click", () => {
		let tableTr = document.querySelectorAll("#data-table tbody tr");
		tableTr = [...tableTr];
		const reverseTr = tableTr.reverse();
		tableBody.replaceChildren(...reverseTr);
	});
});