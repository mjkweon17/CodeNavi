CREATE TABLE `User` (
	`user_id`	INT	NOT NULL,
	`password`	VARCHAR(255)	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
	`github_id`	VARCHAR(255)	NOT NULL,
	`blog_link`	VARCHAR(255)	NOT NULL,
    PRIMARY KEY (`user_id`)
);

CREATE TABLE `Company` (
	`company_id`	INT	NOT NULL,
	`company_name`	VARCHAR(255)	NOT NULL,
    PRIMARY KEY (`company_id`)
);

CREATE TABLE `Lecture` (
	`lecture_id`	INT	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
	`language`	VARCHAR(255)	NOT NULL	DEFAULT 'korean',
	`title`	VARCHAR(255)	NOT NULL,
	`thumbnail`	VARCHAR(255)	NULL,
	`lecturer`	VARCHAR(255)	NOT NULL,
	`couse_hours`	VARCHAR(255)	NULL,
	`difficulty`	VARCHAR(255)	NULL,
	`company_id`	VARCHAR(255)	NOT NULL,
	`price`	VARCHAR(255)	NULL,
	`discount_rate`	VARCHAR(255)	NULL,
	`introduction`	TEXT	NULL,
    PRIMARY KEY (`lecture_id`),
    FOREIGN KEY (`company_id`) REFERENCES `Company` (`company_id`)
);

CREATE TABLE `Review` (
	`review_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`star`	INT	NOT NULL,
	`good_review`	TEXT	NOT NULL,
	`bad_review`	TEXT	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
	`created_at`	DATETIME	NOT NULL,
    PRIMARY KEY (`review_id`),
    FOREIGN KEY (`lecture_id`) REFERENCES `Lecture` (`lecture_id`),
    FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
);

CREATE TABLE `Bookmark` (
	`bookmark_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL,
    PRIMARY KEY (`bookmark_id`),
    FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),  
    FOREIGN KEY (`lecture_id`) REFERENCES `Lecture` (`lecture_id`)
);

CREATE TABLE `STACK_CATEGORY` (
	`stack_category_id`	INT	NOT NULL,
	`parent_id`	INT	NULL,
	`Field`	INT	NOT NULL,
    PRIMARY KEY (`stack_category_id`),
    FOREIGN KEY (`parent_id`) REFERENCES `STACK_CATEGORY` (`stack_category_id`)
);

CREATE TABLE `LectureStack` (
	`lecture_stack_id`	INT	NOT NULL,
	`stack_category_id`	INT	NOT NULL,
	`lecture_id`	INT	NOT NULL,
    PRIMARY KEY (`lecture_stack_id`),
    FOREIGN KEY (`stack_category_id`) REFERENCES `STACK_CATEGORY` (`stack_category_id`),
    FOREIGN KEY (`lecture_id`) REFERENCES `Lecture` (`lecture_id`)
);

CREATE TABLE `UserStack` (
	`user_stack_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`stack_category_id`	INT	NOT NULL,
    PRIMARY KEY (`user_stack_id`),
    FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`),
    FOREIGN KEY (`stack_category_id`) REFERENCES `STACK_CATEGORY` (`stack_category_id`)
);

CREATE TABLE `BOARD` (
	`board_id`	INT	NOT NULL,
	`user_id`	INT	NOT NULL,
	`title`	VARCHAR(255)	NOT NULL,
	`created_at`	DATETIME	NOT NULL,
	`is_active`	BOOL	NOT NULL	DEFAULT TRUE,
    `content`	TEXT	NOT NULL,
    PRIMARY KEY (`board_id`),
    FOREIGN KEY (`user_id`) REFERENCES `User` (`user_id`)
);