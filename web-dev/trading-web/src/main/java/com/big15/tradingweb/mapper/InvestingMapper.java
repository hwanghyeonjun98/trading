package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.InvestingDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface InvestingMapper {

	List<InvestingDto> investingList(@Param("names") String names, @Param("startDate") String startDate, @Param("endDate") String endDate);

	List<InvestingDto> chartList(@Param("names") String names);

	List<InvestingDto> investingDateSearchList(@Param("names") String names, @Param("startDate") String startDate, @Param("endDate") String endDate);

	List<InvestingDto> dataDefultList();

	List<InvestingDto> dataList(@Param("names") String names);
}
