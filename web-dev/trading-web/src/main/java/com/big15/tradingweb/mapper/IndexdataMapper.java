package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.AccountHistoryDto;
import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.dto.MarketCapDto;
import com.big15.tradingweb.dto.NewsDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface IndexdataMapper {
	List<InvestingDto> kospidata();

	List<NewsDto> newsdata();

	List<MarketCapDto> marketCapRanking();

	List<AccountHistoryDto> accountHistory(@Param("account") String account, @Param("replaceCode") String replaceCode);
}
