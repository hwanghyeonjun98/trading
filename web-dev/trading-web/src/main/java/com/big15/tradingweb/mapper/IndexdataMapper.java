package com.big15.tradingweb.mapper;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;

import com.big15.tradingweb.dto.InvestingDto;

@Mapper
public interface IndexdataMapper {
    List<InvestingDto> kospidata();
}
