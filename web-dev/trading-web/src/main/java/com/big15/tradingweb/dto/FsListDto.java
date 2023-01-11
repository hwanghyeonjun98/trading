package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class FsListDto {
	private String stockCode;
	private String korName;
	private String korAbbrvName;
	private String engName;
	private String mrkCls;
	private String scrCls;
	private String stockType;
}
