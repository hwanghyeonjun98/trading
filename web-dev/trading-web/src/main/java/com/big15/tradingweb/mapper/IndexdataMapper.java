package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.InvestingDto;
import com.big15.tradingweb.dto.MarketCapDto;
import com.big15.tradingweb.dto.NewsDto;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface IndexdataMapper {
	List<InvestingDto> kospidata();


	List<NewsDto> newsdata();

	List<MarketCapDto> marketCapRanking();
}
