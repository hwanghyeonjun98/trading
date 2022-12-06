package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.mapper.InvestingMapper;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class TradingRestController {
	private InvestingMapper mapper;

	public TradingRestController(InvestingMapper mapper) {
		this.mapper = mapper;
	}

	@RequestMapping("/api/data/{names}/{startDate}/{endDate}")
	public List<InvestingDto> investingList(@PathVariable("names") String names, @PathVariable("startDate") String startDate, @PathVariable("endDate") String endDate) {
		return mapper.investingList(names, startDate, endDate);
	}

	@RequestMapping("/api/data/dateSearch/{names}/{startDate}/{endDate}")
	public List<InvestingDto> investingDateSearchList(@PathVariable("names") String names, @PathVariable("startDate") String startDate, @PathVariable("endDate") String endDate) {
		return mapper.investingDateSearchList(names, startDate, endDate);
	}

	@RequestMapping("/api/data/chart/{names}")
	public List<InvestingDto> chartList(@PathVariable("names") String names) {
		return mapper.chartList(names);
	}


}
