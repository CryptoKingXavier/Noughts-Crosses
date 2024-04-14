$(document).ready(() => {

    class TicTacToe {
        constructor() {
            this.player_choice = "O"
            this.root = $("#root")[0]
            this.computer_choice = "X"
            this.available = new Array()
            this.game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
            this.board_entry(5, this.computer_choice)
        }

        // Check Win
        check_win = () => {
            // Row-Checker
            // Row-1
            if (this.game_board[0].every((cell) => cell === "X")) return "Computer Wins!"
            else if (this.game_board[0].every((cell) => cell === "O")) return "Player Wins!"

            // Row-2
            if (this.game_board[1].every((cell) => cell === "X")) return "Computer Wins!"
            else if (this.game_board[1].every((cell) => cell === "O")) return "Player Wins!"

            // Row-3
            if (this.game_board[2].every((cell) => cell === "X")) return "Computer Wins!"
            else if (this.game_board[2].every((cell) => cell === "O")) return "Player Wins!"

            // Column-Checker
            // Column-1
            if (this.game_board[0][0] === "X" && this.game_board[1][0] === "X" && this.game_board[2][0] === "X") return "Computer Wins!"
            else if (this.game_board[0][0] === "O" && this.game_board[1][0] === "O" && this.game_board[2][0] === "O") return "Player Wins!"

            // Column-2
            if (this.game_board[0][1] === "X" && this.game_board[1][1] === "X" && this.game_board[2][1] === "X") return "Computer Wins!"
            else if (this.game_board[0][1] === "O" && this.game_board[1][1] === "O" && this.game_board[2][1] === "O") return "Player Wins!"

            // Column-3
            if (this.game_board[0][2] === "X" && this.game_board[1][2] === "X" && this.game_board[2][2] === "X") return "Computer Wins!"
            else if (this.game_board[0][2] === "O" && this.game_board[1][2] === "O" && this.game_board[2][2] === "O") return "Player Wins!"

            // Diagonal-Checker
            // Left-Diagonal
            if (this.game_board[0][0] === "X" && this.game_board[1][1] === "X" && this.game_board[2][2] === "X") return "Computer Wins!"
            else if (this.game_board[0][0] === "O" && this.game_board[1][1] === "O" && this.game_board[2][2] === "O") return "Player Wins!"

            // Right-Diagonal
            if (this.game_board[0][2] === "X" && this.game_board[1][1] === "X" && this.game_board[2][0] === "X") return "Computer Wins!"
            else if (this.game_board[0][2] === "O" && this.game_board[1][1] === "O" && this.game_board[2][0] === "O") return "Player Wins!"
        }

        // Board Design
        board_design = () => {
            this.root.innerHTML = ""
            const section = document.createElement("section")
            section.style.borderRadius = "15px"
            section.className = "m-auto p-2"
            const pre = document.createElement("pre")
            pre.style.color = "snow"
            pre.innerHTML = `
+-------+-------+-------+
|       |       |       |
|   ${this.game_board[0][0]}   |   ${this.game_board[0][1]}   |   ${this.game_board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   ${this.game_board[1][0]}   |   ${this.game_board[1][1]}   |   ${this.game_board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   ${this.game_board[2][0]}   |   ${this.game_board[2][1]}   |   ${this.game_board[2][2]}   |
|       |       |       |
+-------+-------+-------+
`
            section.appendChild(pre)
            this.root.appendChild(section)
        }

        // Board Entry
        board_entry = (position, state) => {
            for (let row of this.game_board) {
                if (row.includes(position)) row[row.indexOf(position)] = state
            }
        }

        // Available Slots
        get_available = () => {
            this.available = []
            this.game_board.forEach((row) => {
                row.forEach((cell) => {
                    if (!isNaN(cell)) this.available.push(cell)
                })
            })
        }

        // Compute Entry
        compute_entry = (position = null, state_ref) => {
            this.get_available()

            if (this.available.length !== 0 && this.check_win() !== "Computer Wins!" && this.check_win() !== "Player Wins!") {
                if (state_ref === "Computer") {
                    let randIdx = Math.floor(Math.random() * ((this.available.length - 1) - 0 + 1)) + 0                    
                    this.board_entry(this.available[randIdx], this.computer_choice)
                } else if (state_ref === "Player") {
                    if (this.available.includes(position)) this.board_entry(position, this.player_choice)
                }
            }
        }

        // Check Draw
        check_draw = () => {
            // Check if any cell is still a number
            for (let i = 0; i < this.game_board.length; i++) {
                for (let j = 0; j < this.game_board[i].length; j++) {
                    if (typeof this.game_board[i][j] === 'number') return false
                }
            }

            // Check if there is a winner
            if (this.check_win() === "Computer Wins!" || this.check_win() === "Player Wins!") return false

            return true; // No empty cells and no winner, game is a draw
        }

        custom_prompt = (text) => {
            $("#prompt_input")[0].placeholder = text
            $("#custom_prompt")[0].classList.remove("d-none")
            return new Promise((resolve, reject) => {
                $("#prompt_button")[0].onclick = () => {
                    resolve($("#prompt_input")[0].value)
                    $("#custom_prompt")[0].classList.add("d-none")
                }
            })
        }

        // Gameplay
        gameplay = async () => {
            while (!this.check_draw()) {
                this.get_available()
                this.board_design()

                // User Input
                const div = document.createElement("div")
                div.className = "d-none mx-auto mb-3 text-center w-75 d-flex align-items-center justify-content-around"
                div.id = "custom_prompt"

                const input = document.createElement("input")
                input.id = "prompt_input"
                input.className = "form-control col-6 font-italic font-weight-bold"

                const button = document.createElement("button")
                button.id = "prompt_button"
                button.innerHTML = "OK"
                button.style.color = "brown"
                button.className = "btn btn-light font-weight-bold"

                div.appendChild(input)
                div.appendChild(button)
                $("section")[$("section")["length"] - 1].appendChild(div)

                let position = await this.custom_prompt("Enter your move")

                while (!this.available.includes(Number.parseInt(position.trim()))) {
                    alert("⛔ Invalid Position! ⛔")
                    $("#prompt_input")[0].value = ""
                    position = await this.custom_prompt("Enter your move")

                    if (this.available.includes(Number.parseInt(position.trim()))) break
                }

                $("#prompt_input")[0].value = ""
                this.compute_entry(Number.parseInt(position.trim()), "Player")
                this.board_design()

                // Computer Input
                this.compute_entry(null, "Computer")

                // Endloop on Win
                if (this.check_win() === "Computer Wins!" || this.check_win() === "Player Wins!") {
                    alert(`${this.check_win()} 🔥`)
                    break
                }

                // Endloop on Draw
                if (this.check_draw()) {
                    console.info("Tie 🔥! Game Over...")
                    break
                }
            }
        }
    }

    
    // Game Instance
    new TicTacToe().gameplay()

})
