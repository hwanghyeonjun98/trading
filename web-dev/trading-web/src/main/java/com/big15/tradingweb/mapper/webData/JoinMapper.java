package com.big15.tradingweb.mapper.webData;

import com.big15.tradingweb.dto.UserInfoDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface JoinMapper {

	List<UserInfoDto> idCheck(@Param("user_id") String user_id);

	int join(@Param("user_id") String user_id
		, @Param("user_pw") String user_pw
		, @Param("user_name") String user_name
		, @Param("user_account_name") String user_account_name
		, @Param("user_account") String user_account);

	void createTable(@Param("sql") String sql);
}
