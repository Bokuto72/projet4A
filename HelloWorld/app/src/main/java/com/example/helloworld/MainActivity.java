package com.example.helloworld;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Référence au TextView
        TextView helloTextView = findViewById(R.id.helloTextView);

        // Afficher "Hello World" dans le TextView
        helloTextView.setText("Hello World");
    }
}
