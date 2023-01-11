package com.big15.tradingweb;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.jdbc.core.JdbcTemplate;

import javax.annotation.Resource;
import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.Statement;

@SpringBootApplication
public class TradingWebApplication {

	@Autowired
	@Resource(name = "webdata")
	private DataSource webdata;

	@Autowired
	@Resource(name = "fsdata")
	private DataSource fsdata;

	@Autowired
	JdbcTemplate template;

	public static void main(String[] args) {
		SpringApplication.run(TradingWebApplication.class, args);
	}

//	@Override
	public void run(String... args) throws Exception   {
		try (Connection connection = webdata.getConnection()) {
			System.out.println(connection.getMetaData().getURL());

			Statement statement = connection.createStatement();

			String sql = "CREATE TABLE TEST1(age INTEGER, name VARCHAR(255))";
			statement.execute(sql);

		}

		try (Connection connection = fsdata.getConnection()) {
			System.out.println(connection.getMetaData().getURL());

			Statement statement = connection.createStatement();

			String sql = "CREATE TABLE TEST2(age INTEGER, name VARCHAR(255))";
			statement.execute(sql);
		}
	}

}
