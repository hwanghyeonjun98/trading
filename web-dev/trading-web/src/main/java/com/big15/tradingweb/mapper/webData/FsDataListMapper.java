package com.big15.tradingweb.mapper.webData;

import com.big15.tradingweb.dto.FsListDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface FsDataListMapper {
	List<FsListDto> stockList();
	List<FsListDto> stockSearchList(@Param("fsData") String fsData);
}
