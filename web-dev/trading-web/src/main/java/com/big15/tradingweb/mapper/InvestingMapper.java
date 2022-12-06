package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.InvestingDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface InvestingMapper {
    @Select("SELECT DATE_FORMAT(dates, '%Y-%m-%d') as dates, closes, opens, highs, lows, volumes, changes FROM ${names} ORDER BY dates desc ")
    List<InvestingDto> investingList(@Param("names") String names);

    @Select("SELECT DATE_FORMAT(dates, '%Y-%m-%d') as dates, closes, opens, highs, lows, volumes, changes FROM ${names} ORDER BY ${base} ${sorts}")
    List<InvestingDto> sortList(@Param("names") String names, @Param("base") String base, @Param("sorts") String sorts);
}
