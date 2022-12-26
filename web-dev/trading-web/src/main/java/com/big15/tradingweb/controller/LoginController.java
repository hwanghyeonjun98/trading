package com.big15.tradingweb.controller;

import com.big15.tradingweb.mapper.LoginMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Slf4j
@Controller
@AllArgsConstructor
//@RequestMapping("")
public class LoginController {
	private LoginMapper loginMapper;
	@GetMapping("/login")
	public String loginPage() {
		return "/login/login";
	}
}
