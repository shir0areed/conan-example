# conan-example

## Essential commands
  - for conan 1.X
      ```
    conan install path/to/repo -if path/to/build_dir
    conan build path/to/repo -bf path/to/build_dir
    ```
  - for conan 2.X
      ```
    conan install path/to/repo -of path/to/build_dir
    conan build path/to/repo -of path/to/build_dir
    ```

## Example
  - Windows Command Prompt
  - conan 1.61
  - In-source build
    ```
    mkdir .\build
    echo * > .\build\.gitignore
    conan install . -if .\build
    conan build . -bf .\build
    ```
