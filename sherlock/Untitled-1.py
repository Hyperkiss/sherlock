{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Pyright CLI",
            "type": "node",
            "request": "launch",
            "program": "${workspaceRoot}/packages/pyright/index.js",
            "preLaunchTask": "npm: build:cli:dev",
            "args": [
                "--verifytypes",
                "pandas.core.reshape.concat",
            ],
            "internalConsoleOptions": "openOnSessionStart",
            "outFiles": [
                "${workspaceRoot}/packages/pyright/dist/**/*.js"
            ]
        },
        {
            "name": "Pyright tests",
            "type": "node",
            "request": "launch",
            "args": [
                "--runInBand"
            ],
            "cwd": "${workspaceRoot}/packages/pyright-internal",
            "console": "integratedTerminal",
            "internalConsoleOptions": "neverOpen",
            "program": "${workspaceFolder}/packages/pyright-internal/node_modules/jest/bin/jest"
        },
        {
            "name": "Pyright extension",
            "type": "extensionHost",
            "request": "launch",
            "runtimeExecutable": "${workspaceRoot}/packages/vscode-pyright/dist/extension.js",
            "preLaunchTask": "npm: build:extension:dev",
            "args": [
                "--extensionDevelopmentPath=${workspaceFolder}/packages/vscode-pyright",
                // The published extension is named "ms-pyright.pyright", but in debug mode it's "ms-pyright.vscode-pyright"
                // to allow the extension code to participate in the lerna monorepo. Make sure that the published extension
                // isn't enabled, otherwise both are loaded and conflict.
                "--disable-extension=ms-pyright.pyright"
            ],
            "smartStep": true,
            "sourceMaps": true,
            "outFiles": [
                "${workspaceRoot}/packages/vscode-pyright/dist/**/*.js"
            ]
        },
        {
            "name": "Pyright extension (watch)",
            "type": "extensionHost",
            "request": "launch",
            "runtimeExecutable": "${workspaceRoot}/packages/vscode-pyright/dist/extension.js",
            "preLaunchTask": "Watch extension",
            "args": [
                "--extensionDevelopmentPath=${workspaceFolder}/packages/vscode-pyright",
                // The published extension is named "ms-pyright.pyright", but in debug mode it's "ms-pyright.vscode-pyright"
                // to allow the extension code to participate in the lerna monorepo. Make sure that the published extension
                // isn't enabled, otherwise both are loaded and conflict.
                "--disable-extension=ms-pyright.pyright"
            ],
            "smartStep": true,
            "sourceMaps": true,
            "outFiles": [
                "${workspaceRoot}/packages/vscode-pyright/dist/**/*.js"
            ]
        },
        {
            "name": "Pyright attach server",
            "type": "node",
            "request": "attach",
            "port": 6600,
            "smartStep": true,
            "sourceMaps": true,
            "outFiles": [
                "${workspaceRoot}/packages/vscode-pyright/dist/**/*.js"
            ]
        },
        {
            "name": "Pyright jest current file",
            "type": "node",
            "request": "launch",
            "args": [
                "${fileBasenameNoExtension}",
                "--runInBand",
            ],
            "cwd": "${workspaceRoot}/packages/pyright-internal",
            "console": "integratedTerminal",
            "internalConsoleOptions": "neverOpen",
            "program": "${workspaceFolder}/packages/pyright-internal/node_modules/jest/bin/jest"
        },
        {
            "name": "Pyright jest selected test",
            "type": "node",
            "request": "launch",
            "args": ["${fileBasenameNoExtension}", "--runInBand", "-t", "${selectedText}"],
            "cwd": "${workspaceRoot}/packages/pyright-internal",
            "console": "integratedTerminal",
            "internalConsoleOptions": "neverOpen",
            "program": "${workspaceFolder}/packages/pyright-internal/node_modules/jest/bin/jest"
        },
        {
            "name": "Pyright fourslash current file",
            "type": "node",
            "request": "launch",
            "args": [
                "fourSlashRunner.test.ts",
                "-t ${fileBasenameNoExtension}",
                "--runInBand",
            ],
            "cwd": "${workspaceRoot}/packages/pyright-internal",
            "console": "integratedTerminal",
            "internalConsoleOptions": "neverOpen",
            "program": "${workspaceFolder}/packages/pyright-internal/node_modules/jest/bin/jest"
        }
    ]
}
