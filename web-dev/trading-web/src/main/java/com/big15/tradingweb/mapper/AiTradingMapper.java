package com.big15.tradingweb.mapper;

import com.big15.tradingweb.dto.AccountDto;
import com.big15.tradingweb.dto.AccountHistoryDto;
import com.big15.tradingweb.dto.AiTradingDto;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;

import java.util.List;

@Mapper
public interface AiTradingMapper {
	List<AiTradingDto> aiTradingData(@Param("account") String account);

	List<AccountHistoryDto> accountHistory(@Param("account") String account,
	                                       @Param("stock_code") String stock_code
	);

	List<AccountHistoryDto> accountHistorySearch(@Param("account") String account,
	                                             @Param("stock_code") String stock_code,
	                                             @Param("start_date") String start_date,
	                                             @Param("end_date") String end_date
	);

	List<AccountHistoryDto> historyData(@Param("account") String account);

	List<AccountHistoryDto> allHistoryDataSearch(@Param("account") String account,
	                                             @Param("start_date") String start_date,
	                                             @Param("end_date") String end_date,
	                                             @Param("code") String code);
	List<AccountHistoryDto> coList(@Param("account") String account);
	List<AccountHistoryDto> profit(@Param("account") String account);
	List<AccountDto> accountChartList(@Param("account") String account);

}
