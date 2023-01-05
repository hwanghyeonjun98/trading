package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class AccountDto {
	private String date;
	private String acc_name;
	private int acc_value;
	private String ratio;
	private String kospi_changes;
	private String kosdaq_changes;
}
