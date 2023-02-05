pipeline{
    agent {
        label 'slave-win'
    }

    stages{
        stage('获取源码') {
            parallel {
                stage('安卓程序源码') {
                    steps {
                        script {
                            echo  '安卓程序源码'
                            bat "git clone git@github.com:xiaoxiangard/AndroidSampleApp.git"
                        } 
                    }
                }

                stage('自动化测试程序源码') {
                    steps {
                        script {
                            echo  '自动测试程序源码'
                            bat "git clone git@github.com:xiaoxiangard/SimpleAppPipeline.git"
                        } 
                    }
                }
            }
        }

        stage('安卓编译打包') {
            steps {
                script {
                    echo  '安卓编译打包'
                    bat '''
                        cd AndroidSampleApp
                        gradlew clean assembleDebug
                    '''
                }                 
            }
        }

        stage('测试与发布') {
            parallel {
                stage('发布测试包') {
                    steps {
                        archiveArtifacts artifacts: 'AndroidSampleApp/app/build/outputs/apk/debug/app-debug.apk'
                    }
                }

                stage('自动化'){
                    stages{
                        stage('部署') {
                            steps {
                                script {
                                    echo  '自动化部署'
                                    bat '''
                                        cd AndroidSampleApp/app/build/outputs/apk/debug
                                        adb install app-debug.apk                                       
                                    '''
                                }                
                            }
                        }

                        stage('自动化测试') {
                            steps {
                                script {
                                    echo  '运行自动化测试'
                                    bat '''
                                        cd SimpleAppPipeline/TestCases
                                        python -m pytest test_bvt.py
                                    '''
                                }  
                            }
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            emailext body: '$DEFAULT_CONTENT', recipientProviders: [[$class: 'RequesterRecipientProvider']], subject: '$DEFAULT_SUBJECT'
        }
    }
}