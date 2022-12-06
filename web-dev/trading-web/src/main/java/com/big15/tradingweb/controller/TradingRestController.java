package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.mapper.InvestingMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;

@RestController
public class TradingRestController {
	private InvestingMapper mapper;

	public TradingRestController(InvestingMapper mapper) {
		this.mapper = mapper;
	}

	@RequestMapping("/api/data/{names}")
	public List<InvestingDto> investingList(@PathVariable("names") String names) {
		return mapper.investingList(names);
	}

	@RequestMapping("/api/data/chart/{names}")
	public List<InvestingDto> chartList(@PathVariable("names") String names) {
		return mapper.investingList(names);
	}


}
