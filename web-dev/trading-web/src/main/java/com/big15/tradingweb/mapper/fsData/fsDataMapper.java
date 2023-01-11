package com.big15.tradingweb.mapper.fsData;

import com.big15.tradingweb.dto.FsDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface fsDataMapper {
	List<FsDto> fsInfoList(@Param("fsData") String fsData);
}
