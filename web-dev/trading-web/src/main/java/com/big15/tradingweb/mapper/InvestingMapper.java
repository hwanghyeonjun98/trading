package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.InvestingDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.springframework.web.bind.annotation.PathVariable;

import java.util.List;

@Mapper
public interface InvestingMapper {

    List<InvestingDto> investingList(@Param("names") String names);

    List<InvestingDto> chartList(@Param("names") String names);

    List<InvestingDto> investingSortList(@Param("names") String names, @Param("base") String base, @Param("sorts") String sorts);

    List<InvestingDto> dataList();
}
