package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.*;
import com.big15.tradingweb.mapper.AiTradingMapper;
import com.big15.tradingweb.mapper.IndexdataMapper;
import com.big15.tradingweb.mapper.InvestingMapper;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Slf4j
@RestController
@RequestMapping("/api/data")
public class TradingRestController {
	@Autowired
	private InvestingMapper mapper;
	@Autowired
	private AiTradingMapper aiTradingData;
	@Autowired
	private IndexdataMapper indexdataMapper;

	public TradingRestController(InvestingMapper mapper) {
		this.mapper = mapper;
	}

	@RequestMapping("/dateSearch/{names}/{startDate}/{endDate}")
	public List<InvestingDto> investingDateSearchList(@PathVariable("names") String names,
	                                                  @PathVariable("startDate") String startDate,
	                                                  @PathVariable("endDate") String endDate) {
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

	@RequestMapping("/index/chart/account/{account}")
	public List<AccountDto> accountChartList(@PathVariable("account") String account) {
		return aiTradingData.accountChartList(account);
	}

	@RequestMapping("/aiTradingData/{account}")
	public List<AiTradingDto> aiTradingData(@PathVariable("account") String account) {
		return aiTradingData.aiTradingData(account);
	}

	@RequestMapping("/allHistoryData/{account}")
	public List<AccountHistoryDto> historyData(@PathVariable("account") String account) {
		return aiTradingData.historyData(account);
	}

	@RequestMapping("/allHistoryDataSearch/{account}/{startDate}/{endDate}/{code}")
	public List<AccountHistoryDto> allHistoryDataSearch(@PathVariable("account") String account,
	                                                    @PathVariable("startDate") String startDate,
	                                                    @PathVariable("endDate") String endDate,
	                                                    @PathVariable("code") String code
	) {
		return aiTradingData.allHistoryDataSearch(account, startDate, endDate, code);
	}

	@RequestMapping("/coList/{account}")
	public List<AccountHistoryDto> coList(@PathVariable("account") String account) {
		return aiTradingData.coList(account);
	}

	@RequestMapping("/coListSearch/{account}/{stock_code}")
	public List<AccountHistoryDto> coListSearch(@PathVariable("account") String account,
	                                            @PathVariable("stock_code") String stock_code) {
		return aiTradingData.accountHistory(account, stock_code);
	}


	@RequestMapping("/profit/{account}")
	public List<AccountHistoryDto> coListSearch(@PathVariable("account") String account) {
		return aiTradingData.profit(account);
	}

	@RequestMapping("/marketCapRanking")
	public List<MarketCapDto> marketCapRanking() {
		return indexdataMapper.marketCapRanking();
	}

	@RequestMapping("/accountHistory/{account}/{stock_code}")
	public List<AccountHistoryDto> accountHistory(@PathVariable("account") String account,
	                                              @PathVariable("stock_code") String stock_code
	) {
		return aiTradingData.accountHistory(account, stock_code);
	}

	@RequestMapping("/accountHistorySearch/{account}/{stock_code}/{start_date}/{end_date}")
	public List<AccountHistoryDto> accountHistorySearch(@PathVariable("account") String account,
	                                                    @PathVariable("stock_code") String stock_code,
	                                                    @PathVariable("start_date") String start_date,
	                                                    @PathVariable("end_date") String end_date
	) {
		return aiTradingData.accountHistorySearch(account, stock_code, start_date, end_date);
	}

}
