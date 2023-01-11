package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.UserInfoDto;
import com.big15.tradingweb.mapper.webData.LoginMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@Slf4j
@RestController
@AllArgsConstructor
public class LoginRestcontroller {

	private LoginMapper loginMapper;

	@RequestMapping("/login/userLogin")
	public void login(@RequestParam("user_id") String user_id,
	                  @RequestParam("user_pw") String user_pw,
	                  HttpServletRequest request,
	                  HttpServletResponse response) {
		try {
			HttpSession session = request.getSession(true);

			UserInfoDto user = loginMapper.login(user_id);

			if (user != null && user_id.equals(user.getUser_id()) && user_pw.equals(user.getUser_pw())) {
				session.setAttribute("userName", user.getUser_name());
				session.setAttribute("userAccount", user.getUser_account());
				response.getWriter().print(true);
			} else {
				response.getWriter().print(false);
			}
		} catch (IOException | NullPointerException e) {
			throw new RuntimeException(e);
		}
	}
}
