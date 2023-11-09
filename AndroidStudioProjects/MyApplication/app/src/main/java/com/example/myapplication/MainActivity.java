package com.example.myapplication;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.GridLayout;
import android.widget.ImageView;

public class ReversiGameActivity extends Activity {
    private static final int BOARD_SIZE = 8;
    private ImageView[][] board;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_reversi_game);

        GridLayout gridLayout = findViewById(R.id.gridLayout);
        board = new ImageView[BOARD_SIZE][BOARD_SIZE];

        for (int row = 0; row < BOARD_SIZE; row++) {
            for (int col = 0; col < BOARD_SIZE; col++) {
                board[row][col] = new ImageView(this);
                board[row][col].setImageResource(R.drawable.empty_square);
                GridLayout.LayoutParams params = new GridLayout.LayoutParams();
                params.width = 100; // Adjust the size as needed
                params.height = 100;
                board[row][col].setLayoutParams(params);
                gridLayout.addView(board[row][col]);
            }
        }

        Button restartButton = findViewById(R.id.restartButton);
        restartButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Implement your restart logic here
            }
        });
    }
}
