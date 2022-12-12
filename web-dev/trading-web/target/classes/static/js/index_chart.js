let chartUrl = "/api/data/chart/" + tableName + "코스피지수";

  $.getJSON(chartUrl, function (response) {
		let dataList = [];

		response.forEach((item) => {
			dataList.push([item.dates, item.opens, item.highs, item.lows, item.closes]);
		});

		chart.updateSeries([{
			name : "table",
			data : dataList
		}]);
	});
