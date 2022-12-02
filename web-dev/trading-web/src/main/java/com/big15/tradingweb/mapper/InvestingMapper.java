package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.InvestingDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

@Mapper
public interface InvestingMapper {
    @Select("select * from ${names}")
    List<InvestingDto> investingList(@PathVariable("names") String names);
}
