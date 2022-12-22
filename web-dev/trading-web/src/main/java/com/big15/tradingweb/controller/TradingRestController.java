package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.AiTradingDto;
import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.dto.MarketCapDto;
import com.big15.tradingweb.mapper.AiTradingMapper;
import com.big15.tradingweb.mapper.IndexdataMapper;
import com.big15.tradingweb.mapper.InvestingMapper;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/api/data")
public class TradingRestController {
	@Autowired
	private InvestingMapper mapper;
	@Autowired
	private AiTradingMapper tradingMapper;

	@Autowired
	private IndexdataMapper indexdataMapper;

	public TradingRestController(InvestingMapper mapper) {
		this.mapper = mapper;
	}

	@RequestMapping("/dateSearch/{names}/{startDate}/{endDate}")
	public List<InvestingDto> investingDateSearchList(@PathVariable("names") String names, @PathVariable("startDate") String startDate, @PathVariable("endDate") String endDate) {
		return mapper.investingDateSearchList(names, startDate, endDate);
	}

	@RequestMapping("/chart/{names}")
	public List<InvestingDto> chartList(@PathVariable("names") String names) {
		return mapper.chartList(names);
	}

	@RequestMapping("/index/chart/kospi")
	public List<InvestingDto> kospiChartList() {
		return mapper.kospiChartList();
	}

	@RequestMapping("/aiTradingData") // 더미 데이터
	public List<AiTradingDto> aiTradingData() {
		return tradingMapper.aiTradingData();
	}

	@RequestMapping("/marketCapRanking")
	public List<MarketCapDto> marketCapRanking() {
		return indexdataMapper.marketCapRanking();
	}
}
