package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.mapper.InvestingMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.logging.LogLevel;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
@Slf4j
@RestController
public class TradingRestController {
	private InvestingMapper mapper;

	public TradingRestController(InvestingMapper mapper) {
		this.mapper = mapper;
	}

	@RequestMapping("/api/data/dateSearch/{names}/{startDate}/{endDate}")
	public List<InvestingDto> investingDateSearchList(@PathVariable("names") String names, @PathVariable("startDate") String startDate, @PathVariable("endDate") String endDate) {
		return mapper.investingDateSearchList(names, startDate, endDate);
	}

	@RequestMapping("/api/data/chart/{names}")
	public List<InvestingDto> chartList(@PathVariable("names") String names) {
		return mapper.chartList(names);
	}

	@RequestMapping("/api/data/chart/kospi")
	public List<InvestingDto> kospiChartList() {
		return mapper.kospiChartList();
	}

}
