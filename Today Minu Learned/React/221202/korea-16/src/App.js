import ball from './assets/ball.png';
import 대한민국 from './assets/korea.png';
import 포르투갈 from './assets/portugal.png';
import 가나 from './assets/ghana.png';
import 우루과이 from './assets/uruguay.png';
import { useState, useEffect } from 'react'
import './App.css';


function App() {
  const [ gameScore, setGameScore ] = useState([0, 0, 0, 0])
  const [ scoreBoard, setScoreBoard ] = useState([
    { name: '포르투갈', win: 2, draw: 1, lose: 0, getGoal: 5, loseGoal: 2 },
    { name: '가나', win: 1, draw: 1, lose: 1, getGoal: 5, loseGoal: 5 },
    { name: '대한민국', win: 0, draw: 2, lose: 1, getGoal: 2, loseGoal: 3 },
    { name: '우루과이', win: 0, draw: 2, lose: 1, getGoal: 0, loseGoal: 2 },
  ])

  const [ possible, setPossible ] = useState(null)

  useEffect(() => {
    const 대한민국 = gameScore[0]
    const 포르투갈 = gameScore[1]
    const 가나 = gameScore[2]
    const 우루과이 = gameScore[3]

    if (대한민국 > 포르투갈) {
      // 우루과이가 가나를 이기는 경우
      if (우루과이 > 가나) {
        if (우루과이 === 3 && 가나 === 1 && 대한민국 === 1 && 포르투갈 === 0) {
          setPossible('16강 진출 미정')
        } else if (우루과이 === 4 && 가나 === 2 && 대한민국 === 2 && 포르투갈 === 1) {
          setPossible('16강 진출 미정')
        } else if (우루과이 === 4 && 가나 === 1 && 대한민국 === 2 && 포르투갈 === 0) {
          setPossible('16강 진출 미정')
        // 우루과이가 3점차 이상으로 이기고, 대한민국이 1점차로 이기면 탈락
        } else if (우루과이 - 가나 > 2 && 대한민국 - 포르투갈 < 2) {
          setPossible('16강 진출 실패')
        // 우루과이가 4점차로 이기고, 대한민국이 2점차 이하로 이기면 탈락
        } else if (우루과이 - 가나 > 3 && 대한민국 - 포르투갈 < 3) {
          setPossible('16강 진출 실패')
        // 1:0, 4:2의 경우 탈락
        } else if (우루과이 === 4 && 가나 === 2 && 대한민국 === 1 && 포르투갈 === 0) {
          setPossible('16강 진출 실패')
        } else {
          setPossible('16강 진출 성공!')
        }

      // 우루과이와 가나가 비기는 경우
      } else if (우루과이 === 가나) {
        // 4:3, 0:0 상황일 경우 진출
        if (우루과이 === 0 && 가나 === 0 && 대한민국 === 4 && 포르투갈 === 3) {
          setPossible('16강 진출 성공!')
        // 우리나라가 2점차 이상으로 이기면 진출
        } else if (대한민국 - 포르투갈 > 1) {
          setPossible('16강 진출 성공!')
        // 그 외 실패
        } else {
          setPossible('16강 진출 실패')
        }
      
      // 가나가 우루과이를 이기는 경우
      } else if (우루과이 < 가나) {
        setPossible('16강 진출 실패')
      }

    } else {
      setPossible('16강 진출 실패')
    }
  }, [gameScore])

  useEffect(() => {
    console.log(possible)
  }, [possible])

  return (
    <div className="App">
      <header className="App-header">
        <img src={ball} className="App-logo" alt="logo" />
        <p>
          H조 16강 경우의 수 계산기
        </p>
        <Game1 team1="대한민국" team2="포르투갈"></Game1>
        <Game2 team1="가나" team2="우루과이"></Game2>
        <div id="possible">대한민국 {possible}</div>
        <a id='git' href='https://github.com/minu-j'>Github minu-j</a>
        <Table scoreBoard={scoreBoard}></Table>
        <div id='info'>* 승점, 골득실만 반영횐 순위표이므로 정확하지 않을 수 있습니다.</div>
      </header>
    </div>
  );

  function Table(props) {
    let rows = []
    for (let i = 0; i < props.scoreBoard.length; i++) {
      const row = props.scoreBoard[i]
      rows.push(
        <Row 
          key={i} 
          name={row.name} 
          win={row.win} 
          draw={row.draw} 
          lose={row.lose} 
          getGoal={row.getGoal} 
          loseGoal={row.loseGoal}
        ></Row>)
    }
    return (
      <div>
        <FirstRow></FirstRow>
        {rows}
      </div>
    )
    function FirstRow() {

      return (
        <div className='row'>
          <div className='row-title'></div>
          <div className='row-num'>승점</div>
          <div className='row-num'>승</div>
          <div className='row-num'>무</div>
          <div className='row-num'>패</div>
          <div className='row-num'>골득실</div>
        </div>
      )
    }
    
    function Row(props) {
      let totalScore = props.win * 3 + props.draw
      let goalScore = props.getGoal - props.loseGoal
      
      return (
        <div className='row'>
          <div className='row-title'>{props.name}</div>
          <div className='row-num'>{totalScore}</div>
          <div className='row-num'>{props.win}</div>
          <div className='row-num'>{props.draw}</div>
          <div className='row-num'>{props.lose}</div>
          <div className='row-num'>{goalScore}</div>
        </div>
      )
    }
    
  }
  function Game1(props) {

    return (
      <div className='game'>
        <span className='game-score'>
          <img className='game-score-img' src={대한민국} alt="대한민국"></img>
          <span className='game-score-name'>{props.team1}</span>
          <span className='game-score-name'>{gameScore[0]}</span>
          <select className='game-score-input' onChange={ event => {
            event.preventDefault()
            setGameScore(gameScore => {
              let newGameScore = [...gameScore]
              newGameScore[0] = parseInt(event.target.value)
              return newGameScore
            })
            const newScoreBoard = [...scoreBoard]
            for (let i = 0; i < newScoreBoard.length; i++) {
              if (newScoreBoard[i].name === "대한민국") {
                newScoreBoard[i].getGoal = 2 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[1]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1 + 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) > gameScore[1]) {
                  newScoreBoard[i].win = 0 + 1
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) < gameScore[1]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1 + 1
                }

              } else if (newScoreBoard[i].name === "포르투갈") {
                newScoreBoard[i].loseGoal = 2 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[1]) {
                  newScoreBoard[i].win = 2
                  newScoreBoard[i].draw = 0 + 1
                  newScoreBoard[i].lose = 0
                } else if (parseInt(event.target.value) > gameScore[1]) {
                  newScoreBoard[i].win = 2
                  newScoreBoard[i].draw = 0
                  newScoreBoard[i].lose = 0 + 1
                } else if (parseInt(event.target.value) < gameScore[1]) {
                  newScoreBoard[i].win = 2 + 1
                  newScoreBoard[i].draw = 0
                  newScoreBoard[i].lose = 0
                }

              }
            }
            newScoreBoard.sort((a, b) => {
              const aGoalScore = a.getGoal - a.loseGoal
              const bGoalScore = b.getGoal - b.loseGoal
              if (aGoalScore > bGoalScore) {
                return -1
              }
              if (aGoalScore < bGoalScore) {
                return 1
              }
              return 0
            })
            newScoreBoard.sort((a, b) => {
              const aTotalScore = a.win * 3 + a.draw
              const bTotalScore = b.win * 3 + b.draw
              if (aTotalScore > bTotalScore) {
                return -1
              }
              if (aTotalScore < bTotalScore) {
                return 1
              }
              return 0
            })
            setScoreBoard(newScoreBoard)
          }}>
            <option value="">...</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
          </select>
        </span>
        <span>
          VS
        </span>
        <span className='game-score'>
        <img className='game-score-img' src={포르투갈} alt="포르투갈"></img>
        <span className='game-score-name'>{props.team2}</span>
        <span className='game-score-name'>{gameScore[1]}</span>
          <select className='game-score-input' onChange={ event => {
            event.preventDefault()
            setGameScore(gameScore => {
              let newGameScore = [...gameScore]
              newGameScore[1] = parseInt(event.target.value)
              return newGameScore
            })
            const newScoreBoard = [...scoreBoard]
            for (let i = 0; i < newScoreBoard.length; i++) {
              if (newScoreBoard[i].name === "포르투갈") {
                newScoreBoard[i].getGoal = 5 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[0]) {
                  newScoreBoard[i].win = 2
                  newScoreBoard[i].draw = 0 + 1
                  newScoreBoard[i].lose = 0
                } else if (parseInt(event.target.value) > gameScore[0]) {
                  newScoreBoard[i].win = 2 + 1
                  newScoreBoard[i].draw = 0
                  newScoreBoard[i].lose = 0
                } else if (parseInt(event.target.value) < gameScore[0]) {
                  newScoreBoard[i].win = 2
                  newScoreBoard[i].draw = 0
                  newScoreBoard[i].lose = 0 + 1
                }

              } else if (newScoreBoard[i].name === "대한민국") {
                newScoreBoard[i].loseGoal = 3 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[0]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1 + 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) > gameScore[0]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1 + 1
                } else if (parseInt(event.target.value) < gameScore[0]) {
                  newScoreBoard[i].win = 0 + 1
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1
                }
              }
            }
            newScoreBoard.sort((a, b) => {
              const aGoalScore = a.getGoal - a.loseGoal
              const bGoalScore = b.getGoal - b.loseGoal
              if (aGoalScore > bGoalScore) {
                return -1
              }
              if (aGoalScore < bGoalScore) {
                return 1
              }
              return 0
            })
            newScoreBoard.sort((a, b) => {
              const aTotalScore = a.win * 3 + a.draw
              const bTotalScore = b.win * 3 + b.draw
              if (aTotalScore > bTotalScore) {
                return -1
              }
              if (aTotalScore < bTotalScore) {
                return 1
              }
              return 0
            })
            setScoreBoard(newScoreBoard)
          }}>
            <option value="">...</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
          </select>
        </span>
      </div>
    )
  }
  
  function Game2(props) {
    return (
      <div className='game'>
        <span className='game-score'>
          <img className='game-score-img' src={가나} alt="가나"></img>
          <span className='game-score-name'>{props.team1}</span>
          <span className='game-score-name'>{gameScore[2]}</span>
          <select className='game-score-input' onChange={ event => {
            event.preventDefault()
            setGameScore(gameScore => {
              let newGameScore = [...gameScore]
              newGameScore[2] = parseInt(event.target.value)
              return newGameScore
            })
            const newScoreBoard = [...scoreBoard]
            for (let i = 0; i < newScoreBoard.length; i++) {
              if (newScoreBoard[i].name === "가나") {
                newScoreBoard[i].getGoal = 5 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[3]) {
                  newScoreBoard[i].win = 1
                  newScoreBoard[i].draw = 0 + 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) > gameScore[3]) {
                  newScoreBoard[i].win = 1 + 1
                  newScoreBoard[i].draw = 0
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) < gameScore[3]) {
                  newScoreBoard[i].win = 1
                  newScoreBoard[i].draw = 0
                  newScoreBoard[i].lose = 1 + 1
                }

              } else if (newScoreBoard[i].name === "우루과이") {
                newScoreBoard[i].loseGoal = 2 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[3]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1 + 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) > gameScore[3]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1 + 1
                } else if (parseInt(event.target.value) < gameScore[3]) {
                  newScoreBoard[i].win = 0 + 1
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1
                }
              }
            }
            newScoreBoard.sort((a, b) => {
              const aGoalScore = a.getGoal - a.loseGoal
              const bGoalScore = b.getGoal - b.loseGoal
              if (aGoalScore > bGoalScore) {
                return -1
              }
              if (aGoalScore < bGoalScore) {
                return 1
              }
              return 0
            })
            newScoreBoard.sort((a, b) => {
              const aTotalScore = a.win * 3 + a.draw
              const bTotalScore = b.win * 3 + b.draw
              if (aTotalScore > bTotalScore) {
                return -1
              }
              if (aTotalScore < bTotalScore) {
                return 1
              }
              return 0
            })
            setScoreBoard(newScoreBoard)
          }}>
            <option value="">...</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
          </select>
        </span>
        <span>
          VS
        </span>
        <span className='game-score'>
        <img className='game-score-img' src={우루과이} alt="우루과이"></img>
        <span className='game-score-name'>{props.team2}</span>
        <span className='game-score-name'>{gameScore[3]}</span>
          <select className='game-score-input' onChange={ event => {
            event.preventDefault()
            setGameScore(gameScore => {
              let newGameScore = [...gameScore]
              newGameScore[3] = parseInt(event.target.value)
              return newGameScore
            })
            const newScoreBoard = [...scoreBoard]
            for (let i = 0; i < newScoreBoard.length; i++) {
              if (newScoreBoard[i].name === "우루과이") {
                newScoreBoard[i].getGoal = 0 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[2]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1 + 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) > gameScore[2]) {
                  newScoreBoard[i].win = 0 + 1
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) < gameScore[2]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1 + 1
                }

              } else if (newScoreBoard[i].name === "가나") {
                newScoreBoard[i].loseGoal = 5 + parseInt(event.target.value)

                if (parseInt(event.target.value) === gameScore[2]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1 + 1
                  newScoreBoard[i].lose = 1
                } else if (parseInt(event.target.value) > gameScore[2]) {
                  newScoreBoard[i].win = 0
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1 + 1
                } else if (parseInt(event.target.value) < gameScore[2]) {
                  newScoreBoard[i].win = 0 + 1
                  newScoreBoard[i].draw = 1
                  newScoreBoard[i].lose = 1
                }
              }
            }
            newScoreBoard.sort((a, b) => {
              const aGoalScore = a.getGoal - a.loseGoal
              const bGoalScore = b.getGoal - b.loseGoal
              if (aGoalScore > bGoalScore) {
                return -1
              }
              if (aGoalScore < bGoalScore) {
                return 1
              }
              return 0
            })
            newScoreBoard.sort((a, b) => {
              const aTotalScore = a.win * 3 + a.draw
              const bTotalScore = b.win * 3 + b.draw
              if (aTotalScore > bTotalScore) {
                return -1
              }
              if (aTotalScore < bTotalScore) {
                return 1
              }
              return 0
            })
            setScoreBoard(newScoreBoard)
          }}>
            <option value="">...</option>
            <option value="0">0</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
            <option value="4">4</option>
          </select>
        </span>
      </div>
    )
  }
}

export default App;
