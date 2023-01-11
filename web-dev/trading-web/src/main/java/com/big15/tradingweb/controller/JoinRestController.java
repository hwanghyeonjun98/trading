package com.big15.tradingweb.controller;

import com.big15.tradingweb.dto.UserInfoDto;
import com.big15.tradingweb.mapper.webData.JoinMapper;
import lombok.AllArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@Slf4j
@RestController
@AllArgsConstructor
@RequestMapping("/join")
public class JoinRestController {

	JoinMapper joinMapper;

	@PutMapping("/userJoin")
	public void join(@RequestParam("user_id") String user_id
		, @RequestParam("user_pw") String user_pw
		, @RequestParam("user_name") String user_name
		, @RequestParam("user_account_name") String user_account_name
		, @RequestParam("user_account") String user_account
		, HttpServletResponse response) throws IOException {
		int join = joinMapper.join(user_id, user_pw, user_name, user_account_name, user_account);

		if (join == 0) {
			response.getWriter().print("joinFalse");
		}

		if (join == 1) {
			response.getWriter().print("joinTrue");
			String sql = "CREATE TABLE web_data." + user_account + "_account_status(" +
				"     code text" +
				"   , name text" +
				"   , amount text" +
				"   , buyprice text" +
				"   , evalValue text" +
				"   , ratio text" +
				"   , currentValue text )";

			joinMapper.createTable(sql);
		}
		String redirect_url = "/login";
		response.sendRedirect(redirect_url);
	}

	@RequestMapping("/idCheck/{user_id}")
	public void idCheck(@PathVariable("user_id") String user_id, HttpServletResponse response) throws IOException {
		List<UserInfoDto> user = joinMapper.idCheck(user_id);

		if (user.size() == 0) {
			response.getWriter().print("notId");
		}

		if (user.size() > 0) {
			response.getWriter().print("hadId");
		}
	}
}
