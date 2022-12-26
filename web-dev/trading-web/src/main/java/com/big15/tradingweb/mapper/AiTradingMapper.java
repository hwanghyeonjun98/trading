package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.AiTradingDto;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface AiTradingMapper {
	List<AiTradingDto> aiTradingData();
}
