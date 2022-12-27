package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.UserInfoDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

@Mapper
public interface LoginMapper {
	UserInfoDto login(@Param("user_id") String user_id);
}
