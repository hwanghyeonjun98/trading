const sortBtn = document.querySelectorAll(".sort-btn");

sortBtn.forEach((btn, idx) => {
	btn.addEventListener("click", function tableSort() {
		let rows;
		let x;
		let y;
		let switchCnt = 0;
		let switching = true;
		let shouldSwitch;
		let dir = "asc";
		let table = document.getElementById("data-table");
		while (switching) {
			switching = false;
			rows = table.rows;
			console.log(rows);
			for (let i = 1; i < (rows.length - 1); i++) {
				shouldSwitch = false;
				x = rows[i].getElementsByTagName("td")[idx];
				y = rows[i + 1].getElementsByTagName("td")[idx];
				console.log(x);
				console.log(y);
				if (dir === "asc") {
					if (Number(x.innerText) > Number(y.innerText)) {
						shouldSwitch = true;
						break;
					}
				} else if (dir === "desc") {
					if (Number(x.innerText) < Number(y.innerText)) {
						shouldSwitch = true;
						break;
					}
				}
				if (shouldSwitch) {
					rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
					switching = true;

					switchCnt++;
				} else {
					if (switchCnt === 0 && dir === "asc") {
						dir = "desc";
						switching = true;
					}
				}
			}
		}
	});
});