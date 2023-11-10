## Rising Coder

- [웹 배포 링크]()
- [서버 배포 링크](http://118.67.143.134:8080/)

## 개요
- 역삼역에는 많은 개발자가 있음
- 현업 개발자들뿐만 아니라, 부트캠프 및 학원에서 개발의 꿈을 키우는 사람들이 많음
- 예비 개발자들은 기초를 쌓기 위해 좋은 강의를 듣고 싶어함
- 현업 개발자들도 실력을 키우기 위해 강의를 듣곤 함
- 심지어 개발자로 이직을 꿈꾸거나, 개발에 대해 배우고 싶어하는 다른 직군에서 일하는 사람들도 개발과 관련된 교육에 대한 니즈가 있음
- 하지만 교육 플랫폼도 많은뿐더러, 하나의 플랫폼에도 같은 기술에 대한 강의가 무수히 많아서 역삼역 피플들은 강의를 고르는 데 큰 어려움을 겪곤함
- 그래서 해키토키 팀8은 이러한 어려움을 해결해주고자, 여러 코딩 교육 플랫폼의 강의 목록을 한곳에 모아두고, 필터링을 통해 원하는 강의를 쉽게 찾거나, 사용자들의 생생한 리뷰를 듣고 비교할 수 있는 사이트를 만듦.

## 일정
- 2023년 11월 10일 19시 ~ 2023년 11월 11일 20시


## 💻 Team 8 소개

<table align="center" style = "table-layout: auto; width: 100%; table-layout: fixed;">
  <tr>
    <td>
       <img width="200" src = "https://avatars.githubusercontent.com/u/75142329?v=4" />
    </td>
    <td>
      <img width="200" src = "https://avatars.githubusercontent.com/u/78201530?v=4"/>
    </td>
        <td>
      <img width="200" src = "https://avatars.githubusercontent.com/u/66587876?v=4"/>
    </td>
        <td>
      <img width="200" src = "https://avatars.githubusercontent.com/u/109056278?v=4"/>
    </td>
  </tr> 
  <tr>
    <th align="center">권민재</th>
    <th align="center">명재위</th>
    <th align="center">박성철</th>
    <th align="center">소효은</th>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/mjkweon17">mjkweon17</a>
    </td>
    <td align="center">
      <a href="https://github.com/JayMyong66">JayMyong66</a>
    </td>
        <td align="center">
      <a href="https://github.com/manu1307">manu1307</a>
    </td>
        <td align="center">
      <a href="https://github.com/she0108">she0108</a>
    </td>
  </tr>
    <tr>
    <th align="center" colspan="4">Project Planning</th>
  </tr>

  <tr>
    <th align="center">Backend, CI/CD</th>
    <th align="center">Backend, Data Managing</th>
    <th align="center">Frontend</th>
    <th align="center">Frontend</th>
  </tr>
</table>

## 🛠 Frontend Tech Stack
| Framework | React, Vite |
|:---|:---|
| Language | HTML, CSS, Javascript |
| Deployment | Vercel |

## 🛠 Backend Tech Stack
| Framework | FastAPI |
|:---|:---|
| Language | Python 3.10 |
| Database/ORM | MySQL, Naver Cloud Platform - Cloud DB for MySQL, SQLAlchemy |
| CI/CD | Naver Cloud Platform - Server, Docker, Docker Hub, GitHub Actions |
| ETC | Swagger, Notion, Figma, Discord, [ERDCloud](https://www.erdcloud.com/d/nSaQY4NjMcnwcQ3CM), MySQL Workbench |

## 다이어그램

### Overall Architecture
<img width = "500" src = "https://user-images.githubusercontent.com/75142329/282190612-2089d2e5-0304-4951-aadf-cf3746b17897.png" >

### CI/CD Architecture
<img width = "500" src = "https://user-images.githubusercontent.com/75142329/282190604-7e1598f7-c5ce-4e65-a40a-b88302ce58b6.png" >

### ERD
<img width = "800" src = "https://user-images.githubusercontent.com/75142329/282190854-37fdf2c9-f8c7-4d00-a777-952ea3c7c127.png" >


## 기능 설명

- 로그인
- 회원가입
- 강의 보여주기
    - 강의 제목
    - 강의 썸네일
    - 강의하는 사람
    - 분류(웹 개발, 모바일, 백엔드, etc.)
    - 평점
    - 태그 (사용 스택)
    - 수강시간
    - 난이도
    - 가격 (+할인)
    - 강의 소개, 커리큘럼 등 상세정보
    - 후기 (+인프런 수강평 보러가기)
    - 링크 (인프런에서 보기)
    - 찜버튼
- 보관함
- 마이 페이지
    - 보관함
    - 작성한 수강평 확인하기
    - 기술스택
        - 예: HTML, CSS, Javascript, React, Next.jx, Typescript, TailwindCSS, Zustand
    - 설정, 계정 정보
- 리뷰 작성
    - 수강평 작성
    - 평점
    - 이런 점이 좋았어요
    - 이런 점이 아쉬웠어요
- 검색
- 커뮤니티
    - 게시판: 전체 프론트엔드, 백엔드, 데이터, 머신러닝, 기타

## API 리스트

  <table>
    <tr>
      <th>Method</th>
      <th>Endpoint</th>
      <th>Description</th>
    </tr>
    <tr>
      <td>GET</td>
      <td>/test</td>
      <td>전체 사용자 조회하는 테스트용 API<br>이 API를 통해서 서버가 DB와 잘 연결돼있는지 확인</td>
    </tr>
    <tr>
      <td>POST</td>
      <td>/auth/register</td>
      <td>회원가입</td>
    </tr>
    <tr>
      <td>POST</td>
      <td>/auth/login</td>
      <td>회원가입</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/lecture</td>
      <td>전체 강의 목록 조회</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/lecture/{page_id}</td>
      <td>전체 강의 목록 10개씩 조회</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/lecture/search/all</td>
      <td>키워드를 주면 해당 키워드가 제모에 포함된 강의 목록 ‘전부’ return</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/lecture/search/{page}</td>
      <td>키워드를 주면 해당 키워드가 제모에 포함된 강의 목록 ‘20개’ return</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/lecture/{lecutre_id}</td>
      <td>lecture_id에 맞는 강의 상세 조회</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/users/{user_id}</td>
      <td>user_id에 해당하는 사용자 정보 조회</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/users/{user_id}/bookmarks</td>
      <td>user_id에 해당하는 사용자의 찜목록 조회 (목록임! 리스트임!)</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/users/{user_id}/reviews</td>
      <td>user_id에 해당하는 사용자의 리뷰 목록 조회</td>
    </tr>
    <tr>
      <td>POST</td>
      <td>/reviews</td>
      <td>리뷰 작성</td>
    </tr>
    <tr>
      <td>GET</td>
      <td>/reviews/{reviews_id}</td>
      <td>review_id에 해당하는 리뷰 내용 조회</td>
    </tr>
  </table>