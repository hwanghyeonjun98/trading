package com.big15.tradingweb.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import javax.servlet.http.HttpSession;

@Slf4j
@Controller
public class LoginController {
	@GetMapping("/login")
	public String loginPage(HttpSession session) {
		if(session.getAttribute("userAccount") != null) {
			return "redirect:/";
		}
		return "/login/login";
	}
}
