package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.TradingDto;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface TradingMapper {
	List<TradingDto> aiTradingData();
}
