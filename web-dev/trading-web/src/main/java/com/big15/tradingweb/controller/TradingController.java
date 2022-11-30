package com.big15.tradingweb.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpServletRequest;
import java.util.Locale;

@Controller
@RequestMapping("/")
public class TradingController {

	// 브라우저 체크
	// 브라우저가 인터넷 익스플로러면 다른 브라우저 접속, 다운로드 안내 페이지로 이동
	@GetMapping("/")
	public String browserCheck(HttpServletRequest request, Locale locale, Model model) {
		String userAgent = request.getHeader("User-Agent");

		if (userAgent.indexOf("Trident") > -1) {
			model.addAttribute("msg", "Internet Explorer는 호환되지 않는 브라우저 입니다.");
			return "/errors/browser_info";
		}

		return "index";
	}

	@GetMapping("/dataview/dataview")
	public String dataView (){
		return "/dataview/dataview";
	}
}
