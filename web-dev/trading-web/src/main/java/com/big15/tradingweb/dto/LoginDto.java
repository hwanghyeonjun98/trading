package com.big15.tradingweb.dto;

import lombok.Data;

@Data
public class LoginDto {
	private int user_no;
	private String user_id;
	private String user_pw;
	private String user_name;
	private String user_account;
}
